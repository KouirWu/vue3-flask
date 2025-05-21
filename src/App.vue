<!-- 聊天界面的主容器 -->
<template>
  <div class="chat-container">
    <!-- 聊天界面头部 -->
    <div class="chat-header">
      <h2>智能对话助手</h2>
    </div>
    
    <!-- 消息列表区域 -->
    <div class="chat-messages" ref="messageContainer">
      <!-- 遍历消息数组，根据消息类型显示不同样式 -->
      <div v-for="(message, index) in messages" :key="index" 
           :class="['message', message.type === 'user' ? 'user-message' : 'ai-message']">
        <div class="message-content">
          {{ message.content }}
        </div>
      </div>
    </div>

    <!-- 输入区域 -->
    <div class="chat-input">
      <!-- 文本输入框 -->
      <el-input
        v-model="userInput"
        type="textarea"
        :rows="3"
        placeholder="请输入您的问题..."
        @keydown.enter.prevent="handleEnter"
      />
      <!-- 发送按钮 -->
      <el-button type="primary" @click="sendMessage" :loading="loading">
        发送
      </el-button>
    </div>
  </div>
</template>

<script setup>
// 导入所需的Vue组件和工具
import { ref, onMounted, nextTick } from 'vue'
import { ElMessage } from 'element-plus'

// 定义响应式数据
const messages = ref([]) // 存储聊天消息的数组
const userInput = ref('') // 用户输入框的内容
const loading = ref(false) // 加载状态标志
const messageContainer = ref(null) // 消息容器的引用

// 处理回车键事件
const handleEnter = (e) => {
  // 如果没有按住Shift键，则发送消息
  if (!e.shiftKey) {
    sendMessage()
  }
}

// 滚动到底部的函数
const scrollToBottom = async () => {
  await nextTick() // 等待DOM更新
  if (messageContainer.value) {
    messageContainer.value.scrollTop = messageContainer.value.scrollHeight
  }
}

// 发送消息的主函数
const sendMessage = async () => {
  // 检查输入是否为空
  if (!userInput.value.trim()) {
    ElMessage.warning('请输入消息内容')
    return
  }

  // 获取用户输入的消息
  const userMessage = userInput.value.trim()
  // 将用户消息添加到消息列表
  messages.value.push({
    type: 'user',
    content: userMessage
  })
  
  // 清空输入框并设置加载状态
  userInput.value = ''
  loading.value = true
  
  try {
    // 调用后端API
    const response = await fetch('http://localhost:5000/api/chat', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        message: userMessage
      })
    })

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`)
    }

    let aiResponse = '' // 存储AI的完整响应
    const reader = response.body.getReader()
    const decoder = new TextDecoder()

    while (true) {
      const { done, value } = await reader.read()
      if (done) break

      const chunk = decoder.decode(value)
      const lines = chunk.split('\n').filter(line => line.trim() !== '')

      for (const line of lines) {
        if (line.startsWith('data: ')) {
          try {
            const data = JSON.parse(line.slice(6))
            const content = data.content || ''
            const reasoning = data.reasoning || ''
            aiResponse += content + reasoning

            // 更新UI显示
            const lastMessage = messages.value[messages.value.length - 1]
            if (lastMessage && lastMessage.type === 'ai') {
              lastMessage.content = aiResponse
            } else {
              messages.value.push({
                type: 'ai',
                content: aiResponse
              })
            }
            await scrollToBottom()
          } catch (e) {
            console.error('Error parsing chunk:', e)
          }
        }
      }
    }
  } catch (error) {
    // 错误处理
    ElMessage.error('发送消息失败，请重试')
    console.error('Error:', error)
  } finally {
    // 重置加载状态并滚动到底部
    loading.value = false
    scrollToBottom()
  }
}

// 组件挂载时滚动到底部
onMounted(() => {
  scrollToBottom()
})
</script>

<style scoped>
/* 聊天容器样式 */
.chat-container {
  max-width: 800px;
  margin: 0 auto;
  height: 100vh;
  display: flex;
  flex-direction: column;
  background-color: #f5f5f5;
}

/* 头部样式 */
.chat-header {
  padding: 20px;
  background-color: #409EFF;
  color: white;
  text-align: center;
}

/* 消息列表区域样式 */
.chat-messages {
  flex: 1;
  overflow-y: auto;
  padding: 20px;
}

/* 消息样式 */
.message {
  margin-bottom: 20px;
  display: flex;
}

/* 消息内容样式 */
.message-content {
  max-width: 70%;
  padding: 12px 16px;
  border-radius: 8px;
  word-wrap: break-word;
}

/* 用户消息样式 */
.user-message {
  justify-content: flex-end;
}

/* 用户消息内容样式 */
.user-message .message-content {
  background-color: #409EFF;
  color: white;
}

/* AI消息内容样式 */
.ai-message .message-content {
  background-color: white;
  color: #333;
}

/* 输入区域样式 */
.chat-input {
  padding: 20px;
  background-color: white;
  border-top: 1px solid #eee;
  display: flex;
  gap: 10px;
}

/* 发送按钮样式 */
.chat-input .el-button {
  align-self: flex-end;
}
</style> 
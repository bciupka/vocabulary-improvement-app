<template>
  <section class="UploadFiles">
    <!--In this case it's better to use standard input locally. I want to use element plus library, maybe in the future I will add backend-->
    <VocUpload
      class="UploadFiles__addFile"
      action="The nonexisting endpoint"
      :before-upload="handleBeforeUpload"
    >
      <VocButton type="primary">Click to upload</VocButton>
    </VocUpload>
    <InlineMessage v-show="showInlineMessage" :type="messageType" :message="message"/>
  </section>
</template>
<script lang="ts" setup>
import { ElMessage } from 'element-plus'
import { VocUpload } from '@/core/element-plus/index'
import { useVocabularyTestPageStore } from '@/components/store/vocabulary-test-page-store'
import VocButton from '@/core/element-plus/VocButton.vue'
import InlineMessage from '@/core/InlineMessage.vue'
import { computed, ref } from 'vue'

const store = useVocabularyTestPageStore()
const showInlineMessage = ref(false)
//const isLoadedCorrectly = ref(false);
const messageType = computed(() => (store.fileData && store.isLoadedNewValue ? 'success' : 'error'))
const message = computed(() => store.loadFileMessage)
const handleBeforeUpload = (file) => {
  showInlineMessage.value = true
  if (file.type === 'text/plain') {
    readFileContent(file)
  } else {
    ElMessage.error('Please upload a text file (.txt)')
    store.isLoadedNewValue = false
    store.loadFileMessage = 'Wrong file type'
  }
}

const readFileContent = (file) => {
  const reader = new FileReader()
  const actualData = store.fileData

  reader.onload = (e) => {
    const newData = e.target?.result as string
    store.isLoadedCorrectly(newData)
  }

  reader.readAsText(file)
}
</script>
<style lang="scss">
.UploadFiles {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 60px;
  &__addFile {
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
  }
}
</style>
/**/

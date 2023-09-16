import { defineStore } from 'pinia'
import { computed, ref } from 'vue'

type VocabularyFileData = {
  word: string
  wordTranslation: string[]
}

export const useVocabularyTestPageStore = defineStore('vocabulary', () => {
  const fileData = ref<String>()
  const sortedFileData = ref<VocabularyFileData[]>([])
  const isLoadedNewValue = ref(false)
  const loadFileMessage = ref<String>()
  const isLoadedCorrectly = (data: string | undefined) => {
    if (data !== fileData.value) {
      isLoadedNewValue.value = true
      loadFileMessage.value = 'New text loaded'
    } else {
      isLoadedNewValue.value = false
      loadFileMessage.value = 'Loaded text is the same'
    }
    fileData.value = data
  }
  const sortFileData = () => {
    if (fileData.value === undefined) {
      return
    }
    const wordsWithWhiteSpace: VocabularyFileData[] = fileData.value.split('\r\n').map((line) => {
      const [word, wordTranslations] = line.split('-')
      const wordTranslationArray = wordTranslations.split(',')
      return { word, wordTranslation: wordTranslationArray }
    })

    sortedFileData.value = wordsWithWhiteSpace.map((data) => {
      return {
        word: data.word.trim(),
        wordTranslation: data.wordTranslation.map((data) => data.trim())
      }
    })
  }

  const shuffleWords = (words: string[], randomIndex: number) => {
    const correctAnswer = words[0];
    words[0] = words[randomIndex];
    words[randomIndex] = correctAnswer;
    return words;
  }

  return {
    shuffleWords,
    loadFileMessage,
    isLoadedNewValue,
    isLoadedCorrectly,
    fileData,
    sortedFileData,
    sortFileData
  }
})

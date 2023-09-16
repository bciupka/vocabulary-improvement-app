import { defineStore } from 'pinia'
import { ref } from 'vue'
import axios from "axios";
import type {VocabularyFileData} from "@/components/domain/vocabulary-file-data";

export const useVocabularyTestPageStore = defineStore('vocabulary', () => {
  const fileData = ref<String>()
  const sortedFileData = ref<VocabularyFileData[]>([])
  const isLoadedNewValue = ref(false)
  const loadFileMessage = ref<String>()
  //For now here, later in database
  const correctAnswers = ref<number>(0)
  //For now here, later in database
  const wrongAnswers = ref<number>(0)
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

  const fetchVocabulary = () => {
    axios
        .get('https://jsonplaceholder.typicode.com/posts/1')
        .then((response) => {
         console.log();
        })
  }

  return {
    wrongAnswers,
    correctAnswers,
    shuffleWords,
    loadFileMessage,
    isLoadedNewValue,
    isLoadedCorrectly,
    fileData,
    sortedFileData,
    sortFileData
  }
})

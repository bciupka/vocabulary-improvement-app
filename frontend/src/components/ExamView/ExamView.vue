<template>
  <section class="ExamView">
    <button @click="test1()">test</button>
      <InlineMessage v-show="!showInlineMessage" :type="messageType" message="Please load vocabulary"/>
    <div class="ExamView__exam">
      <VocForm class="ExamView__form" :label-position="'top'">
        <VocRow :justify="'center'" :gutter="20">
          <VocCol :span="9">
            <VocFormItem label="Correct answers">
              <VocButton>{{ correctAnswers }}</VocButton>
            </VocFormItem>
          </VocCol>
          <VocCol :span="6">
            <VocFormItem label="WORD">
                <VocInput v-model="wordToTranslate.word"></VocInput>
            </VocFormItem>
          </VocCol>
          <VocCol :span="9">
            <VocFormItem label="Wrong answers">
              <VocButton>{{ wrongAnswers }}</VocButton>
            </VocFormItem>
          </VocCol>
        </VocRow>
        <VocRow v-if="showExam" class="ExamView__row" :justify="'center'" :gutter="20">
            <VocCol class="ExamView__answers" :span="10" v-for="(item,index) in answers">
                <VocButton @click="choosenAnswer(item)" :ref="index">{{ item }}</VocButton>
            </VocCol>
        </VocRow>
      </VocForm>
    </div>
  </section>
</template>

<script setup lang="ts">
import { VocButton, VocInput, VocForm, VocFormItem, VocRow, VocCol } from '@/core/element-plus'
import {computed, onMounted, ref} from 'vue'
import { useVocabularyTestPageStore } from '@/components/store/vocabulary-test-page-store'
import InlineMessage from "@/core/InlineMessage.vue";
import type {VocabularyFileData} from "@/components/domain/vocabulary-file-data";

const store = useVocabularyTestPageStore();
const answers = ref([])
const wordToTranslate = ref<VocabularyFileData>({
    word: "",
    wordTranslation: [""],
});
const getRandomNumber = (min, max) => {
  return Math.floor(Math.random() * (max - min + 1)) + min
}

const messageType = computed( () => store.sortedFileData.length > 0 ? "success" : "error");
const showInlineMessage = computed( () => !!store.sortedFileData.length > 0)
const showExam = computed( () => answers.value.length > 0)
const correctAnswers = computed( () => store.correctAnswers);
const wrongAnswers = computed( () => store.wrongAnswers);
const choosenAnswer = (answer: string) => {
    if(answer === wordToTranslate.value?.wordTranslation[0]) {
        store.correctAnswers++;
    } else {
        store.wrongAnswers++;
    }
    prepareSetOfAnswersAndWordToTranslate();
}
const getRandomNumberWithExcluded = (min, max, excludedNumbers: number[]) => {
    const randomNumber = Math.floor(Math.random() * (max - min + 1)) + min;
    const isExcluded = excludedNumbers.includes(randomNumber);
    if(!isExcluded) {
        return randomNumber;
    }
    return getRandomNumberWithExcluded(min,max,excludedNumbers);
}

const test1 = () => {
    prepareSetOfAnswersAndWordToTranslate();
}

const prepareSetOfAnswersAndWordToTranslate = () => {
  if(answers.value.length > 0) {
      answers.value.length = 0;
      const wordsAmount = store.sortedFileData.length
      const randomIndex = getRandomNumber(0, wordsAmount - 1)
      const drawnIndexes = [randomIndex];
      const correctAnswer = store.sortedFileData[randomIndex].wordTranslation[0];
      wordToTranslate.value = store.sortedFileData[randomIndex];
      answers.value.push(correctAnswer);

      while (answers.value.length < 4) {
          const randomNumber = getRandomNumberWithExcluded(0, wordsAmount - 1, drawnIndexes);
          drawnIndexes.push(randomNumber);
          const word = store.sortedFileData[randomNumber].wordTranslation[0];
          answers.value.push(word);
      }
      const randomIndexForShuffle = getRandomNumberWithExcluded(0, wordsAmount - 1, [0]);
      answers.value = store.shuffleWords(answers.value, randomIndexForShuffle);
  }
}

onMounted( () => {
    prepareSetOfAnswersAndWordToTranslate();
})
</script>

<style scoped lang="scss">
.ExamView {
  &__row {
    margin: $sizeM 0;
  }
  &__answers {
    margin: $sizeM 0;
  }

  &__exam {
    padding: $sizeXXL + $sizeXXL;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  &__form {
    min-width: 300px;
    width: 50%;
    height: 1600px;
    background: navajowhite;
  }
}
</style>

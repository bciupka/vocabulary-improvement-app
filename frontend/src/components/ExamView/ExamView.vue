<template>
  <section class="ExamView">
    <button @click="test1()">test</button>
    <div class="ExamView__exam">
      <VocForm class="ExamView__form" :label-position="'top'">
        <VocRow :justify="'center'" :gutter="20">
          <VocCol :span="3">
            <VocFormItem label="Remove" style="font-size: 5px">
              <VocButton>+</VocButton>
            </VocFormItem>
          </VocCol>
          <VocCol :span="6">
            <VocFormItem label="WORD">
                <VocInput v-model="wordToTranslate"></VocInput>
            </VocFormItem>
          </VocCol>
          <VocCol :span="3">
            <VocFormItem label="Add">
              <VocButton>-</VocButton>
            </VocFormItem>
          </VocCol>
        </VocRow>
        <VocRow v-if="answers.length > 0" class="ExamView__row" :justify="'center'" :gutter="20">
          <VocCol :span="6">
            <VocButton>{{ answers[0] }}</VocButton>
          </VocCol>
          <VocCol :span="6">
            <VocButton>{{ answers[1] }}</VocButton>
          </VocCol>
        </VocRow>
        <VocRow v-if="answers.length > 0" class="ExamView__row" :justify="'center'" :gutter="20">
          <VocCol :span="6">
            <VocButton>{{ answers[2] }}</VocButton>
          </VocCol>
          <VocCol :span="6">
            <VocButton>{{ answers[3] }}</VocButton>
          </VocCol>
        </VocRow>
      </VocForm>
    </div>
  </section>
</template>

<script setup lang="ts">
import { VocButton, VocInput, VocForm, VocFormItem, VocRow, VocCol } from '@/core/element-plus'
import { computed, ref } from 'vue'
import { useVocabularyTestPageStore } from '@/components/store/vocabulary-test-page-store'

const store = useVocabularyTestPageStore();
const answers = ref([])
const wordToTranslate = ref<String>();
const getRandomNumber = (min, max) => {
  return Math.floor(Math.random() * (max - min + 1)) + min
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
    //store.sortFileData();
    /*const t = [0]
    for(let i = 0 ; i < 3; i++) {
        const a = getRandomNumberWithExcluded(0,3,t);
        t.push(a);
    }
    console.log(t);
     const q = getRandomNumberWithExcluded(0,3,[0]);
     const qq = t[0];
     t[0] = t[q];
     t[q] = qq;
     console.log(
         t
     )
*/
    getAnswer();
    console.log(answers.value.length)
}
const loadFileMessage1 = ref<String>();
const getAnswer = () => {
  const wordsAmount = store.sortedFileData.length
  const randomIndex = getRandomNumber(0, wordsAmount-1)
  const drawnIndexes = [randomIndex];
  console.log(store.sortedFileData[randomIndex])
  const correctAnswer = store.sortedFileData[randomIndex].wordTranslation[0];
  wordToTranslate.value = store.sortedFileData[randomIndex].word;
  answers.value.push(correctAnswer);

  for(let i = 0; i < 3; i++) {
      const randomNumber = getRandomNumberWithExcluded(0, wordsAmount-1, drawnIndexes);
      drawnIndexes.push(randomNumber);
      const word = store.sortedFileData[randomNumber].wordTranslation[0];
      answers.value.push(word);
  }
  const randomIndexForShuffle = getRandomNumberWithExcluded(0,wordsAmount-1,[0]);
  answers.value = store.shuffleWords(answers.value, randomIndexForShuffle);
}
</script>

<style scoped lang="scss">
.ExamView {
  &__row {
    margin-bottom: $sizeM;
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

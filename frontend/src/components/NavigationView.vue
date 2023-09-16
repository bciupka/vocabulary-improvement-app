<template>
  <header class="Navigation">
    <div class="Navigation__button" @click="goToExam">
      <p class="Navigation__description">exam</p>
    </div>
    <div class="Navigation__button" @click="goToAddVocabulary">
      <p class="Navigation__description">upload</p>
    </div>
  </header>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { useVocabularyTestPageStore } from '@/components/store/vocabulary-test-page-store'

const store = useVocabularyTestPageStore()

const router = useRouter()
const goToExam = () => {
  store.sortFileData()
  router.push('/')
}

const goToAddVocabulary = () => {
  router.push('/add')
}
</script>

<style scoped lang="scss">
.Navigation {
  height: 45px;
  width: 100%;
  background-color: $succesMain;
  position: sticky;
  z-index: 1;
  border: solid 2px black;
  display: flex;
  justify-content: center;
  align-items: center;

  &__button {
    height: 100%;
    margin: 0 $sizeS;
    border: solid 2px black;
    width: 80px;
    display: flex;
    justify-content: center;
    align-items: center;

    &:hover {
      cursor: pointer;
      background-color: black;
      color: white;
      font-size: $sizeXL;
      transition:
        background-color 1s,
        color 1s,
        font-size 1s;
    }
  }

  &__description {
    text-transform: uppercase;
    font-weight: 600;
  }
}
</style>

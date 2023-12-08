<template>
  <section class="HomePage">
    <div class="HomePage__container">
      <VocRadioGroup v-model="page">
        <VocRadioButton label="Login" />
        <VocRadioButton label="Register" />
      </VocRadioGroup>
      <PageLogin v-if="showLogin" />
      <PageRegister v-else></PageRegister>
    </div>
  </section>
</template>

<script lang="ts" setup>
import { ref } from 'vue'
import PageLogin from './PageLogin.vue'
import PageRegister from './PageRegister.vue'
import { VocRadioGroup, VocRadioButton } from '@/core/element-plus/index'
import { computed } from '@vue/reactivity'
const page = ref('Login')
const showLogin = computed(() => page.value === 'Login')
</script>

<style scope lang="scss">
.HomePage {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  background-image: url("login.png");

  &__container {
    display: flex;
    justify-content: start;
    align-items: center;
    flex-direction: column;
    height: 600px;
    width: 400px;
  }
}
</style>

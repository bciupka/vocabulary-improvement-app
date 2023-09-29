<template>
    <section class="PageLogin">
        <VocForm class="PageLogin__loginBox" label-position="top">
            <VocFormItem label="login" >
                <VocInput v-model="formRegisterAccessibility.login"></VocInput>
            </VocFormItem>
            <VocFormItem label="email" >
                <VocInput v-model="formRegisterAccessibility.email"></VocInput>
            </VocFormItem>
            <VocFormItem label="password" >
                <VocInput v-model="formRegisterAccessibility.password"></VocInput>
            </VocFormItem>
            <VocFormItem label="repeat password" >
                <VocInput v-model="formRegisterAccessibility.repeatedPassword"></VocInput>
            </VocFormItem>
            <VocFormItem>
                <VocButton type="primary" class="PageLogin__loginButton" @click="register">Login</VocButton>
            </VocFormItem>
        </VocForm>
    </section>
</template>

<script lang="ts" setup>
import { VocForm, VocFormItem, VocInput, VocAlert } from "@/core/element-plus/index";
import { reactive, ref} from "vue";
import VocButton from "@/core/element-plus/VocButton.vue";
import {usePageLoginStore} from "@/components/page-login-store";
import {useVocabularyTestPageStore} from "@/components/store/vocabulary-test-page-store";

import {useRouter} from "vue-router";

const loginName = ref('')
const store = usePageLoginStore();
const testStore = useVocabularyTestPageStore();
const loginEmail = () => {
  //  store.login(formRegisterAccessibility.loginEmail, formRegisterAccessibility.password);
}
const router = useRouter()
const register = () => {
    testStore.testAuth = true;
    router.push('/')
    if(formRegisterAccessibility.password === formRegisterAccessibility.repeatedPassword) {
        const registerForm: RegisterForm = {
            email: formRegisterAccessibility.email,
            login: formRegisterAccessibility.login,
            password: formRegisterAccessibility.password,
        }
        store.register(registerForm);
    } else {

    }
}
const formRegisterAccessibility = reactive({
    email: '',
    login:'',
    password: '',
    repeatedPassword:'',
})
</script>

<style scoped lang="scss">
.PageLogin {
  display: flex;
  justify-content: center;
  align-items: center;

  &__loginBox {
    background: $color-background;
    width: 300px;
    height: 350px;
    padding: 50px;
    border-radius: $sizeS;
  }

  &__loginButton {
    margin-top: $sizeXL;
  }
}
</style>
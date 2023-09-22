<template>
    <section class="PageLogin">
        <VocForm class="PageLogin__loginBox" label-position="top">
            <VocFormItem label="email / login" >
                <VocInput v-model="formRegisterAccessibility.login"></VocInput>
            </VocFormItem>
            <VocFormItem label="password" >
                <VocInput v-model="formRegisterAccessibility.email"></VocInput>
            </VocFormItem>
            <VocFormItem label="email / login" >
                <VocInput v-model="formRegisterAccessibility.name"></VocInput>
            </VocFormItem>
            <VocFormItem label="password" >
                <VocInput v-model="formRegisterAccessibility.surname"></VocInput>
            </VocFormItem>
            <VocFormItem label="email / login" >
                <VocInput v-model="formRegisterAccessibility.password"></VocInput>
            </VocFormItem>
            <VocFormItem label="password" >
                <VocInput v-model="formRegisterAccessibility.repeatedPassword"></VocInput>
            </VocFormItem>

            <VocFormItem>
                <VocButton type="primary" class="PageLogin__loginButton" @click="loginEmail">Login</VocButton>
            </VocFormItem>
        </VocForm>
    </section>
</template>

<script lang="ts" setup>
import { VocForm, VocFormItem, VocInput } from "@/core/element-plus/index";
import { reactive, ref} from "vue";
import VocButton from "@/core/element-plus/VocButton.vue";
import {usePageLoginStore} from "@/components/page-login-store";

const loginName = ref('')
const store = usePageLoginStore();
const loginEmail = () => {
  //  store.login(formRegisterAccessibility.loginEmail, formRegisterAccessibility.password);
}

const formRegisterAccessibility = reactive({
    email: '',
    login:'',
    password: '',
    repeatedPassword:'',
    name:'',
    surname:''
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
    height: 500px;
    padding: 50px;
    border-radius: $sizeS;
  }

  &__loginButton {
    margin-top: $sizeXL;
  }
}
</style>
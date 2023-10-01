<template>
 <section class="PageLogin">
     <VocRadioGroup v-model="radio">
         <VocRadio label="1" size="large" @click="test()">Option A</VocRadio>
         <VocRadio  label="2" size="large">Option A</VocRadio>
     </VocRadioGroup>
     <VocForm class="PageLogin__loginBox" label-position="top">
         <VocFormItem label="email / login" >
            <VocInput v-model="formLoginAccessibility.loginEmail"></VocInput>
         </VocFormItem>
         <VocFormItem label="password" >
             <VocInput v-model="formLoginAccessibility.password"></VocInput>
         </VocFormItem>
         <VocFormItem>
             <VocButton type="primary" class="PageLogin__loginButton" @click="loginEmail">Login</VocButton>
         </VocFormItem>
     </VocForm>
<!--     <PageRegister></PageRegister>-->
 </section>
</template>

<script lang="ts" setup>
import { VocForm, VocFormItem, VocInput, VocRadioGroup, VocRadio } from "@/core/element-plus/index";
import { reactive, ref} from "vue";
import VocButton from "@/core/element-plus/VocButton.vue";
import {usePageLoginStore} from "@/components/page-login-store";
import PageRegister from "@/components/PageRegister.vue";
const test = () => {console.log("test")}
const radio = ref("1");
const loginName = ref('')
const store = usePageLoginStore();
const loginEmail = () => {
   store.login(formLoginAccessibility.loginEmail, formLoginAccessibility.password);
}

const formLoginAccessibility = reactive({
    loginEmail: '',
    password: '',
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
    height: 220px;
    padding: 50px;
    border-radius: $sizeS;
  }

  &__loginButton {
    margin-top: $sizeXL;
  }
}
</style>
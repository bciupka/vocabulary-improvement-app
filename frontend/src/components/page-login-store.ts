import {defineStore} from "pinia";
import {ref} from "vue";
import axios from "axios";


export const usePageLoginStore = defineStore('login', () => {

    const login = (loginEmail: string, password: string)  => {
        const response = ref<Boolean>();
        /*axios.post("enpoint", { login: loginEmail })
            .then((response) => {
                console.log(response);
            })*/
    }

    const register = (registerForm: RegisterForm) => {
      console.log(registerForm)
        /*axios.post("enpoint", { registerForm })
           .then((response) => {
               console.log(response);
           })*/
    }

    return {
        login,
        register
    }
})

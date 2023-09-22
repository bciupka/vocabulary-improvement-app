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

    return {
        login
    }
})

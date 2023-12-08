import { defineStore } from 'pinia'
import {ref} from "vue";

export const useAuthenticationStore = defineStore('authentication', () => {
    const auth = ref(false);
    return {
        auth
    }
})

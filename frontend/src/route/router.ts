import VocabularyTestPageView from '@/components/VocabularyTestPageView.vue'
import ExamView from '@/components/ExamView/ExamView.vue'
import UploadVocabulary from '@/components/AddVocabulary/UploadVocabulary.vue'
import type { RouteRecordRaw } from 'vue-router'
import PageLogin from "@/components/PageLogin.vue";
export const routes: Array<RouteRecordRaw> = [
  { path: '/', name: 'VocabularyTestPageView', component: VocabularyTestPageView },
  { path: '/add', name: 'Add', component: UploadVocabulary },
  { path: '/login', name: 'PageLogin', component: PageLogin }
]

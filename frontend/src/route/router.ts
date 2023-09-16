import VocabularyTestPageView from '@/components/VocabularyTestPageView.vue'
import ExamView from '@/components/ExamView/ExamView.vue'
import UploadVocabulary from '@/components/AddVocabulary/UploadVocabulary.vue'
import type { RouteRecordRaw } from 'vue-router'
export const routes: Array<RouteRecordRaw> = [
  { path: '/', name: 'ExamView', component: ExamView },
  { path: '/add', name: 'Add', component: UploadVocabulary }
]

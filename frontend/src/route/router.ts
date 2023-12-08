import VocabularyTestPageView from '@/components/VocabularyTestPageView.vue'
import ExamView from '@/components/ExamView/ExamView.vue'
import UploadVocabulary from '@/components/AddVocabulary/UploadVocabulary.vue'
import type { RouteRecordRaw } from 'vue-router'
import HomePage from "@/components/Home/HomePage.vue";
import {createRouter, createWebHistory} from "vue-router";
import {useVocabularyTestPageStore} from "@/components/store/vocabulary-test-page-store";

const routes: Array<RouteRecordRaw> = [
  { path: '/', name: 'VocabularyTestPageView', component: VocabularyTestPageView },
  { path: '/add', name: 'Add', component: UploadVocabulary },
  { path: '/login', name: 'HomePage', component: HomePage }
]

export { routes };

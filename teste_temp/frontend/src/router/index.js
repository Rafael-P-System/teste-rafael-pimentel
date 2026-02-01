import { createRouter, createWebHistory } from "vue-router";
import OperadorasTable from "../components/OperadorasTable.vue";
import OperadoraDetalhes from "../components/OperadoraDetalhes.vue";

const routes = [
  { path: "/", component: OperadorasTable },
  { path: "/operadora/:cnpj", component: OperadoraDetalhes, props: true }
];

export default createRouter({
  history: createWebHistory(),
  routes
});

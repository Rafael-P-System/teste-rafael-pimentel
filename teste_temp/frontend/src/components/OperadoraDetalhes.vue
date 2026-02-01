<template>
  <div v-if="operadora">
    <h2>Detalhes da Operadora</h2>
    <p><strong>CNPJ:</strong> {{ operadora.cnpj }}</p>
    <p><strong>Razão Social:</strong> {{ operadora.razao_social }}</p>
    <p><strong>UF:</strong> {{ operadora.uf }}</p>
    <p><strong>Despesa:</strong> R$ {{ operadora.despesa.toLocaleString("pt-BR") }}</p>
  </div>
</template>

<script>
import api from "../services/api";

export default {
  name: "OperadoraDetalhes",
  props: ["cnpj"],
  data() {
    return { operadora: null };
  },
  mounted() {
    api.get(`/operadoras/${this.cnpj}`).then(res => {
      this.operadora = res.data;
    });
  }
};
</script>

<style>
h2 {
  margin-top: 20px;
  color: #333;
}
p {
  margin: 5px 0;
}
</style>

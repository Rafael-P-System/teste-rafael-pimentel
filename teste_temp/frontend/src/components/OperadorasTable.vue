<template>
  <div>
    <h2>Operadoras</h2>
    <table>
      <thead>
        <tr>
          <th>CNPJ</th>
          <th>Razão Social</th>
          <th>UF</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="o in operadoras" :key="o.cnpj">
          <td>{{ o.cnpj }}</td>
          <td>{{ o.razao_social }}</td>
          <td>{{ o.uf }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import api from "../services/api";

export default {
  name: "OperadorasTable",
  data() {
    return { operadoras: [] };
  },
  async mounted() {
    const resp = await api.get("/operadoras");
    this.operadoras = resp.data;
  }
};
</script>

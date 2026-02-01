<template>
  <div>
    <h2>Despesas por UF</h2>
    <canvas id="grafico"></canvas>
  </div>
</template>

<script>
import { Chart } from "chart.js";
import api from "../services/api";

export default {
  name: "GraficoDespesas",
  async mounted() {
    const resp = await api.get("/estatisticas");
    const dados = resp.data.por_uf;

    new Chart(document.getElementById("grafico"), {
      type: "bar",
      data: {
        labels: Object.keys(dados),
        datasets: [{
          label: "Despesas",
          data: Object.values(dados),
          backgroundColor: "rgba(75, 192, 192, 0.6)"
        }]
      }
    });
  }
};
</script>

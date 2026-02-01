<template>
  <div id="app">
    <h1>Dashboard de Saúde</h1>

    <div class="card">
      <EstadosIBGE />
    </div>

    <div class="card">
      <OperadorasTable />
    </div>

    <div class="card">
      <GraficoDespesas />
    </div>
  </div>
</template>

<script>
import EstadosIBGE from "./components/EstadosIBGE.vue";
import OperadorasTable from "./components/OperadorasTable.vue";
import GraficoDespesas from "./components/GraficoDespesas.vue";

export default {
  name: "App",
  components: {
    EstadosIBGE,
    OperadorasTable,
    GraficoDespesas
  }
};
</script>

<style>
#app {
  font-family: Arial, sans-serif;
  margin: 20px;
  background-color: #f9f9f9;
}

h1 {
  text-align: center;
  margin-bottom: 2rem;
  color: #333;
}

.card {
  background: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 6px rgba(0,0,0,0.15);
  padding: 20px;
  margin-bottom: 2rem;
}
</style>

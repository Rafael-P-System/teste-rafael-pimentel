<template>
  <div id="app">
    <h1>Dashboard</h1>
    <EstadosIBGE />
    <OperadorasTable />
  </div>
</template>

<script>
import EstadosIBGE from "./components/EstadosIBGE.vue";
import OperadorasTable from "./components/OperadorasTable.vue";

export default {
  name: "App",
  components: {
    EstadosIBGE,
    OperadorasTable
  }
};
</script>

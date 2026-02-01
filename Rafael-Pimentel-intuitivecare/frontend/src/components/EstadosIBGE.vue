<template>
  <div>
    <h2>Estados do Brasil (IBGE)</h2>
    <ul>
      <li v-for="estado in estados" :key="estado.id">{{ estado.nome }}</li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "EstadosIBGE",
  data() {
    return {
      estados: []
    };
  },
  async mounted() {
    const resp = await fetch("https://servicodados.ibge.gov.br/api/v1/localidades/estados");
    this.estados = await resp.json();
  }
};
</script>

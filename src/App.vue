<template>

  <div class="total-header">
    <div>Cancle</div>
    <div><img alt="Vue logo" src="./assets/img/logo.png"></div>
    <div>Next</div>
  </div>

  <div class="total-body">
    <MainContainVue />
  </div>

  <div class="total-footer">
    <div>Cancle</div>
    <div></div>
    <div>Next</div>
  </div>
  
</template>

<script>
import MainContainVue from './components/MainContainView.vue';

export default {
  name: 'App',
  components: {
    MainContainVue
  }
}
</script>

<style>
body {
  margin:0px;
  padding: 0px;
  display: flex;
  align-items: center;
  flex-direction: column;
  justify-content: space-between;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  width: 430px;
  height: 932px;
}

.total-header, .total-footer {
  width: 100%;
  height: 50px;
  background: rgb(130, 161, 133);
  display: flex;
  justify-content: space-between;
  align-items: center;
  /* padding: 5px 10px; */
}
.total-header div, .total-footer div{
  padding: 5px 10px;
  color: rgb(198, 198, 240);
  font-size: 17px;;
}

.total-header img {
  width: 30px;
}

.total-body {
  height: 832px;
  display: flex;
}

</style>

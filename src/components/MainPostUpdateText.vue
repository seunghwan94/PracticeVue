<template>
  <div :class="`upload-image ${filter}`" :style="{ 'background-image': `url(${uploadImg})` }"></div>
  <div class="write">
    <textarea @input="$emit('write',$event.target.value)" class="write-box">write!</textarea>
  </div>
</template>

<script>
export default {
    props:{
        uploadImg:String,
        filter:String,
    }
}
</script>

<style>

.write-box {
border: none;
width: 90%;
height: 100px;
padding: 15px;
margin: auto;
display: block;
outline: none;
}
</style>
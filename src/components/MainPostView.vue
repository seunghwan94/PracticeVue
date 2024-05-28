<template>
  <div style="margin-bottom: 35px;">
    <div class="post-header">
        <div class="post-header-img">
            <img alt="Vue 1" src="../assets/img/1.jpg">
        </div>
        <div class="post-header-text">
            test
        </div>
    </div>
    <div class="post-body"></div>
    <div class="post-footer">
        <div class="post-footer-text">
            <div class="post-footer-main">main-title</div>
            
            <div class="post-footer-sub">sub-title</div>
        </div>
        
        <div class="post-footer-date">May 05 24</div>
    </div>
  </div>
</template>

<script>
export default {

}
</script>

<style>
.post-header {
    display: flex;
    align-items: center;
    margin:20px;
}
.post-header-img {
    width: 50px; 
    height: 50px;
    overflow: hidden; /* 이미지가 컨테이너를 넘치지 않게 하기 위해 */
}
.post-header-img img{
    width: 100%;
    height: 100%;
    border-radius: 50%;
    object-fit: cover;
}
.post-header-text {
    padding-left: 15px;
    font-size: 17px;
    font-weight: bold;
}
.post-body {
    width: 100%;
    height: 300px; /* 예시 높이, 원하는 높이로 설정 */
    background-image: url('../assets/img/2.jpg');
    background-size: cover; /* 배경 이미지를 요소에 맞게 조정 */
    background-position: center; /* 배경 이미지의 위치를 중앙으로 */
    background-repeat: no-repeat; /* 배경 이미지 반복 방지 */
}
.post-footer {
    display: flex;
    margin: 20px;
    flex-direction: column;
    align-items: flex-start;
}
.post-footer-text{
    display: flex;
    align-items: center;
}
.post-footer-main {
    font-size: 20px;
    font-weight: bold;
    padding-right: 10px;
}
.post-footer-date {
    font-size: 13px;
    color: gray;
    margin-top: 10px;
}
</style>
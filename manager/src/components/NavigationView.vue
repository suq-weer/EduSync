<template>
  <ul>
    <li href="#"><RouterLink to="/">主页</RouterLink></li>
  </ul>
  <br />
</template>
<style>
ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  border-top-style: solid;
  border-top-color: blue;
  border-bottom-style: solid;
  border-bottom-color: blue;
}
li {
  float: left;
}
li a {
  display: block;
  color: white;
  text-align: center;
  text-decoration: none;
  padding: 14px 16px;
}
li a:hover {
  color: blue;
}
</style>

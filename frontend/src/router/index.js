import Vue from "vue";
import VueRouter from "vue-router";
import Dashboard from "../views/Dashboard";
import Downloads from "../views/Downloads";
const Help = () => import("../views/Help");

Vue.use(VueRouter);

const routes = [
  {
    path: "/Dashboard",
    name: "Dashboard",
    component: Dashboard
  },
  {
    name: "Downloads",
    path: "/Downloads",
    component: Downloads
  },
  {
    name: "Help",
    path: "/Help",
    component: Help
  },
  {
    // This is a hack to use :to tag for absolute paths.
    path: "/http*",
    beforeEnter: to => {
      window.open(to.fullPath.substring(1), "_blank");
    }
  },
  { path: "*", redirect: "/Dashboard" }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;

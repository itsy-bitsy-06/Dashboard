import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    socketMessage: "",
    searchInput: "",
    inverted: false,
    isSearchVisible: false
  },
  mutations: {
    UPDATED(state, message) {
      state.socketMessage = message;
    },
    SEARCH(state, payload) {
      state.isSearchVisible = payload.visible;
      state.inverted = payload.inverted;
      state.searchInput = payload.value;
    }
  },
  actions: {
    setSearch(context, payload) {
      context.commit("SEARCH", payload);
    }
  },
  modules: {}
});

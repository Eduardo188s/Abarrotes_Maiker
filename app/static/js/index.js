const App = {
  components: {
    EasyDataTable: window['vue3-easy-data-table'],
  },
  methods:{
    AgregarProducto:function(){
this.items.push( { "nombre_producto": "Aceite", "cantidad_compra": 3, "total_compra": 77, "total": 77 })
    }
  },
  data () {
    return {
      headers:[
        { text: "Producto", value: "nombre_producto" },
        { text: "Cantidad", value: "cantidad_compra", sortable: true },
        { text: "Subtotal", value: "total_compra", sortable: true },
        { text: "Total", value: "total", sortable: true }
      ],
      items: [

      ],
    }
  },
};
Vue.createApp(App).mount('#app');
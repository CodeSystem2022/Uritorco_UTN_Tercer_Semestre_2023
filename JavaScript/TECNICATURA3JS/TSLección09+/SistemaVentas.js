class Producto{

    static contadorProductos = 0;

    constructor(nombre, precio) {
        this._idProducto = ++Producto.contadorProductos;
        this._nombre = nombre;
        this._precio = precio;
    }

    get idProducto() {
        return this._idProducto;
    }

    get nombre() {
        return this._nombre;
    }

    set nombre(nombre) {
        this._nombre = nombre;
    }

    get precio() {
        return this._precio;
    }

    set precio(precio) {
        this._precio = precio;
    }

    toString() { 
        return `idProducto: ${this._idProducto}, nombre: ${this._nombre}, precio: $${this._precio}`;
    }
}


class Orden{
    static contadorOrdenes = 0;
    static getMAX_PRODUCTOS() {
        return 5
    }

    constructor(...productos) { 
        this._idOrden = ++Orden.contadorOrdenes;
        this._contadorProductosAgregados = 0;
        this._productos = [];

        for (let producto of productos) {
            this.agregarProducto(producto);
        }
    }
    
    get idOrden() {
        return this.idOrden;
    }

    agregarProducto(producto) {
        if (this._productos.length < Orden.getMAX_PRODUCTOS()) {
            this._productos.push(producto);
        } else {
            console.log('No se pueden agregar más productos a la orden. Superaste el límite máximo que es 5');
        }
    }

    calcularTotal() {
        let total = 0;
        for(let producto of this._productos) {
            total += producto.precio;
        }
        return total; 
    }

    mostrarOrden() {
        let productosOrden = ' ';
        for (let producto of this._productos) {
            productosOrden += '\n{'+producto.toString() + ' }';
        }
        console.log(`Orden: ${this._idOrden}, Total: $${this.calcularTotal()}, Productos: ${productosOrden}`);
    }
}


let producto1 = new Producto('Pantalon', 200);
let producto2 = new Producto('Camisa', 150);
let producto3 = new Producto('Cinturon', 50);
let orden1 = new Orden();
let orden2 = new Orden();
orden1.agregarProducto(producto1);
orden1.agregarProducto(producto2);
orden1.agregarProducto(producto3);
orden2.agregarProducto(producto1);
orden2.agregarProducto(producto2);
orden2.agregarProducto(producto3);
orden1.mostrarOrden();
orden2.mostrarOrden();
class Cliente extends Persona{

    static contadorClientes = 0;

    constructor(nombre, apellido, edad, fecharegistro){
        super(nombre, apellido, edad);
        this._idCliente = ++Cliente.contadorClientes;
        this._sueldo = fecharegistro;
    }

    get _idCliente(){
        return this._idCliente
    }

    get fecharegistro(){
        return this._fechaRegistro;
    }

    set fecharegistro(fecharegistro){
        this._fechaRegistro = fecharegistro;
    }


    toString(){
        return `
        ${super.toString()} 
        ${this._idCliente}
        ${this._fechaRegistro}`
    }
}
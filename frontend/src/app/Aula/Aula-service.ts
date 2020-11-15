import { Http, RequestOptions, Headers, Response } from "@angular/http";
import { Injectable } from "@angular/core";
import { Observable } from "../../../node_modules/rxjs";
import { AulaModel } from "./Aula-model";
import { RespJsonFlask, BASE_PATH_SERVER } from "../app.api";

const Aula_API = `${BASE_PATH_SERVER}/educat/Aula`


@Injectable()
export class AulaService{

    constructor(private http: Http){
    }

    allAulas():Observable<Response>{
        return this.http.get(
            Aula_API
        )
    }

    saveAula(newItem: AulaModel): void{
        this.http.put(
            Aula_API,
            JSON.stringify(newItem)
        ).subscribe(
            resp => {
                const obj:RespJsonFlask = (<RespJsonFlask>resp.json())
                let data:AulaModel = (<AulaModel>obj.data)
                console.log('"saveAula" = ', data)
            }
        )
    }

}
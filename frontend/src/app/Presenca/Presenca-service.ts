import { Http, RequestOptions, Headers, Response } from "@angular/http";
import { Injectable } from "@angular/core";
import { Observable } from "../../../node_modules/rxjs";
import { PresencaModel } from "./Presenca-model";
import { RespJsonFlask, BASE_PATH_SERVER } from "../app.api";
import { AuthService } from '../shared/auth-service'

const Presenca_API = `${BASE_PATH_SERVER}/educat/Presenca`


@Injectable()
export class PresencaService{

    static currentPresenca: PresencaModel

    static getCurrPresenca(){
        if(PresencaService.currentPresenca){
            return PresencaService.currentPresenca.aula.descricao
        }else{
            return ''
        }
    }

    constructor(private http: Http){
    }

    allPresencas():Observable<Response>{
        return this.http.get(
            Presenca_API
            ,new RequestOptions({headers: AuthService.header})
        )
    }

    PresencasByTitle(text: string):Observable<Response>{
        return this.http.get(
            `${Presenca_API}?aula.descricao=${text}`
            ,new RequestOptions({headers: AuthService.header})
        )
    }

    delete(id: string): void{
        this.http.delete(
            `${Presenca_API}/${id}`
            ,new RequestOptions({headers: AuthService.header})
        ).subscribe(
            resp => {
                const obj:RespJsonFlask = (<RespJsonFlask>resp.json())
                let data:PresencaModel = (<PresencaModel>obj.data)
                console.log('"Presenca.Delete" = ', data)
            }
        )
    }

    savePresenca(newItem: PresencaModel): void{
        this.http.post(
            Presenca_API,
            JSON.stringify(newItem)
            ,new RequestOptions({headers: AuthService.header})
        ).subscribe(
            resp => {
                const obj:RespJsonFlask = (<RespJsonFlask>resp.json())
                let data:PresencaModel = (<PresencaModel>obj.data)
                console.log('"savePresenca" = ', data)
            }
        )
    }

}
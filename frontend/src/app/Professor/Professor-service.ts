import { Http, RequestOptions, Headers, Response } from "@angular/http";
import { Injectable } from "@angular/core";
import { Observable } from "../../../node_modules/rxjs";
import { ProfessorModel } from "./Professor-model";
import { RespJsonFlask, BASE_PATH_SERVER } from "../app.api";
import { AuthService } from '../shared/auth-service'

const Professor_API = `${BASE_PATH_SERVER}/educat/Professor`


@Injectable()
export class ProfessorService{

    static currentProfessor: ProfessorModel

    static getCurrProfessor(){
        if(ProfessorService.currentProfessor){
            return ProfessorService.currentProfessor.nome
        }else{
            return ''
        }
    }

    constructor(private http: Http){
    }

    allProfessors():Observable<Response>{
        return this.http.get(
            Professor_API
            ,new RequestOptions({headers: AuthService.header})
        )
    }

    ProfessorsByTitle(text: string):Observable<Response>{
        return this.http.get(
            `${Professor_API}?nome=${text}`
            ,new RequestOptions({headers: AuthService.header})
        )
    }

    delete(RF: string): void{
        this.http.delete(
            `${Professor_API}/${RF}`
            ,new RequestOptions({headers: AuthService.header})
        ).subscribe(
            resp => {
                const obj:RespJsonFlask = (<RespJsonFlask>resp.json())
                let data:ProfessorModel = (<ProfessorModel>obj.data)
                console.log('"Professor.Delete" = ', data)
            }
        )
    }

    saveProfessor(newItem: ProfessorModel): void{
        this.http.post(
            Professor_API,
            JSON.stringify(newItem)
            ,new RequestOptions({headers: AuthService.header})
        ).subscribe(
            resp => {
                const obj:RespJsonFlask = (<RespJsonFlask>resp.json())
                let data:ProfessorModel = (<ProfessorModel>obj.data)
                console.log('"saveProfessor" = ', data)
            }
        )
    }

}
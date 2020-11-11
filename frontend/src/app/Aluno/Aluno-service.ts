import { Http, RequestOptions, Headers, Response } from "@angular/http";
import { Injectable } from "@angular/core";
import { Observable } from "../../../node_modules/rxjs";
import { AlunoModel } from "./Aluno-model";
import { RespJsonFlask, BASE_PATH_SERVER } from "../app.api";
import { AuthService } from '../shared/auth-service'

const Aluno_API = `${BASE_PATH_SERVER}/educat/Aluno`


@Injectable()
export class AlunoService{

    static currentAluno: AlunoModel

    static getCurrAluno(){
        if(AlunoService.currentAluno){
            return AlunoService.currentAluno.nome
        }else{
            return ''
        }
    }

    constructor(private http: Http){
    }

    allAlunos():Observable<Response>{
        return this.http.get(
            Aluno_API
            ,new RequestOptions({headers: AuthService.header})
        )
    }

    AlunosByTitle(text: string):Observable<Response>{
        return this.http.get(
            `${Aluno_API}?nome=${text}`
            ,new RequestOptions({headers: AuthService.header})
        )
    }

    delete(RA: string): void{
        this.http.delete(
            `${Aluno_API}/${RA}`
            ,new RequestOptions({headers: AuthService.header})
        ).subscribe(
            resp => {
                const obj:RespJsonFlask = (<RespJsonFlask>resp.json())
                let data:AlunoModel = (<AlunoModel>obj.data)
                console.log('"Aluno.Delete" = ', data)
            }
        )
    }

    saveAluno(newItem: AlunoModel): void{
        this.http.post(
            Aluno_API,
            JSON.stringify(newItem)
            ,new RequestOptions({headers: AuthService.header})
        ).subscribe(
            resp => {
                const obj:RespJsonFlask = (<RespJsonFlask>resp.json())
                let data:AlunoModel = (<AlunoModel>obj.data)
                console.log('"saveAluno" = ', data)
            }
        )
    }

}
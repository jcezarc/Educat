import { Component, OnInit } from '@angular/core';
import { AulaModel } from '../Aula-model';
import { AulaService } from '../Aula-service';
import { Router } from '@angular/router';
import {RespJsonFlask} from '../../app.api'
import {AlunoService} from '../../Aluno/Aluno-service'
import {CursoService} from '../../Curso/Curso-service'


@Component({
  selector: 'app-Aula-list',
  templateUrl: './Aula-list.component.html'
})
export class AulaListComponent implements OnInit {

  items: AulaModel[] = []
  
  constructor(
    private AulaSvc: AulaService,
    private router: Router
  ) { }

  ngOnInit() {
    this.router.onSameUrlNavigation = "reload"
    this.AulaSvc.allAulas().subscribe(
      resp => {
        let obj:RespJsonFlask = (<RespJsonFlask>resp.json())
        this.items = (<AulaModel[]>obj.data)
      }
    )
  }

  filter(param: any){
    this.AulaSvc.AulasByTitle(param.searchContent).subscribe(
      resp => {
        let obj:RespJsonFlask = (<RespJsonFlask>resp.json())
        this.items = (<AulaModel[]>obj.data)
      // },error => {
      //   if(error.status == 404) this.items = []
      }
    )
  }

  save(item: AulaModel){
    this.AulaSvc.saveAula(item)
    this.items.push(item)
  }

}

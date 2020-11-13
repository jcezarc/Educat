import { Component, OnInit } from '@angular/core';
import { AulaModel } from '../Aula-model';
import { AulaService } from '../Aula-service';
import { Router } from '@angular/router';
import {RespJsonFlask} from '../../app.api'


@Component({
  selector: 'app-Aula-list',
  templateUrl: './Aula-list.component.html'
})
export class AulaListComponent implements OnInit {

  source: AulaModel[] = []
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
        this.source = (<AulaModel[]>obj.data)
        this.items = this.source
      }
    )
  }

  filter(param: any){
    if(!param.searchContent){
      this.items = this.source
      return
    }
    this.items = this.source.filter(
      (obj: AulaModel) => 
        obj.aluno.nome.contains(param.searchContent)
    )
  }

  save(item: AulaModel){
    this.AulaSvc.saveAula(item)
  }

}

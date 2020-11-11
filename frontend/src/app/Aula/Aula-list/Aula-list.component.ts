import { Component, OnInit } from '@angular/core';
import { AulaModel } from '../Aula-model';
import { AulaService } from '../Aula-service';
import { Router } from '@angular/router';
import {RespJsonFlask} from '../../app.api'
import {ProfessorService} from '../../Professor/Professor-service'


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

  add(){
    this.router.navigate(['/new-Aula'])
  }

  remove(item: AulaModel){
    if(!confirm(`Remove Aula "${item.descricao}" ?`)){
      return
    }
    this.AulaSvc.delete(item.id as unknown as string)
    this.items.splice(this.items.indexOf(item),1)
  }

  save(item: AulaModel){
        item.professor = ProfessorService.currentProfessor

    this.AulaSvc.saveAula(item)
    this.items.push(item)
  }

  select(item: AulaModel){
    AulaService.currentAula = item
    this.router.navigate(['/new-Presenca'])
  }

}

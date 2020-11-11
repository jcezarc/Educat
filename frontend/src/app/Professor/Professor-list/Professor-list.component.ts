import { Component, OnInit } from '@angular/core';
import { ProfessorModel } from '../Professor-model';
import { ProfessorService } from '../Professor-service';
import { Router } from '@angular/router';
import {RespJsonFlask} from '../../app.api'


@Component({
  selector: 'app-Professor-list',
  templateUrl: './Professor-list.component.html'
})
export class ProfessorListComponent implements OnInit {

  items: ProfessorModel[] = []
  
  constructor(
    private ProfessorSvc: ProfessorService,
    private router: Router
  ) { }

  ngOnInit() {
    this.router.onSameUrlNavigation = "reload"
    this.ProfessorSvc.allProfessors().subscribe(
      resp => {
        let obj:RespJsonFlask = (<RespJsonFlask>resp.json())
        this.items = (<ProfessorModel[]>obj.data)
      }
    )
  }

  filter(param: any){
    this.ProfessorSvc.ProfessorsByTitle(param.searchContent).subscribe(
      resp => {
        let obj:RespJsonFlask = (<RespJsonFlask>resp.json())
        this.items = (<ProfessorModel[]>obj.data)
      // },error => {
      //   if(error.status == 404) this.items = []
      }
    )
  }

  add(){
    this.router.navigate(['/new-Professor'])
  }

  remove(item: ProfessorModel){
    if(!confirm(`Remove Professor "${item.nome}" ?`)){
      return
    }
    this.ProfessorSvc.delete(item.RF as unknown as string)
    this.items.splice(this.items.indexOf(item),1)
  }

  save(item: ProfessorModel){
    
    this.ProfessorSvc.saveProfessor(item)
    this.items.push(item)
  }

  select(item: ProfessorModel){
    ProfessorService.currentProfessor = item
    this.router.navigate(['/new-Aula'])
  }

}

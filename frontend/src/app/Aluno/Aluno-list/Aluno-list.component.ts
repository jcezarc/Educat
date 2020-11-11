import { Component, OnInit } from '@angular/core';
import { AlunoModel } from '../Aluno-model';
import { AlunoService } from '../Aluno-service';
import { Router } from '@angular/router';
import {RespJsonFlask} from '../../app.api'


@Component({
  selector: 'app-Aluno-list',
  templateUrl: './Aluno-list.component.html'
})
export class AlunoListComponent implements OnInit {

  items: AlunoModel[] = []
  
  constructor(
    private AlunoSvc: AlunoService,
    private router: Router
  ) { }

  ngOnInit() {
    this.router.onSameUrlNavigation = "reload"
    this.AlunoSvc.allAlunos().subscribe(
      resp => {
        let obj:RespJsonFlask = (<RespJsonFlask>resp.json())
        this.items = (<AlunoModel[]>obj.data)
      }
    )
  }

  filter(param: any){
    this.AlunoSvc.AlunosByTitle(param.searchContent).subscribe(
      resp => {
        let obj:RespJsonFlask = (<RespJsonFlask>resp.json())
        this.items = (<AlunoModel[]>obj.data)
      // },error => {
      //   if(error.status == 404) this.items = []
      }
    )
  }

  add(){
    this.router.navigate(['/new-Aluno'])
  }

  remove(item: AlunoModel){
    if(!confirm(`Remove Aluno "${item.nome}" ?`)){
      return
    }
    this.AlunoSvc.delete(item.RA as unknown as string)
    this.items.splice(this.items.indexOf(item),1)
  }

  save(item: AlunoModel){
    
    this.AlunoSvc.saveAluno(item)
    this.items.push(item)
  }

  select(item: AlunoModel){
    AlunoService.currentAluno = item
    this.router.navigate(['/new-Presenca'])
  }

}

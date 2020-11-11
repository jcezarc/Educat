import { Component, OnInit } from '@angular/core';
import { PresencaModel } from '../Presenca-model';
import { PresencaService } from '../Presenca-service';
import { Router } from '@angular/router';
import {RespJsonFlask} from '../../app.api'
import {AlunoService} from '../../Aluno/Aluno-service'
import {AulaService} from '../../Aula/Aula-service'


@Component({
  selector: 'app-Presenca-list',
  templateUrl: './Presenca-list.component.html'
})
export class PresencaListComponent implements OnInit {

  items: PresencaModel[] = []
  
  constructor(
    private PresencaSvc: PresencaService,
    private router: Router
  ) { }

  ngOnInit() {
    this.router.onSameUrlNavigation = "reload"
    this.PresencaSvc.allPresencas().subscribe(
      resp => {
        let obj:RespJsonFlask = (<RespJsonFlask>resp.json())
        this.items = (<PresencaModel[]>obj.data)
      }
    )
  }

  filter(param: any){
    this.PresencaSvc.PresencasByTitle(param.searchContent).subscribe(
      resp => {
        let obj:RespJsonFlask = (<RespJsonFlask>resp.json())
        this.items = (<PresencaModel[]>obj.data)
      // },error => {
      //   if(error.status == 404) this.items = []
      }
    )
  }

  add(){
    this.router.navigate(['/new-Presenca'])
  }

  remove(item: PresencaModel){
    if(!confirm(`Remove Presenca "${item.aula.descricao}" ?`)){
      return
    }
    this.PresencaSvc.delete(item.id as unknown as string)
    this.items.splice(this.items.indexOf(item),1)
  }

  save(item: PresencaModel){
        item.aluno = AlunoService.currentAluno
    item.aula = AulaService.currentAula

    this.PresencaSvc.savePresenca(item)
    this.items.push(item)
  }

  select(item: PresencaModel){
    PresencaService.currentPresenca = item
    this.router.navigate(['/new-'])
  }

}

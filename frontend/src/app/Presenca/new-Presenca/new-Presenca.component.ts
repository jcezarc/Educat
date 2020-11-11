import { Component, OnInit } from '@angular/core';
import { PresencaModel } from '../Presenca-model';
import { PresencaService } from '../Presenca-service';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import {AlunoService} from '../../Aluno/Aluno-service'
import {AulaService} from '../../Aula/Aula-service'


@Component({
  selector: 'app-new-Presenca',
  templateUrl: './new-Presenca.component.html'
})
export class NewPresencaComponent implements OnInit {

  PresencaForm: FormGroup

  constructor(
    private PresencaSvc: PresencaService,
    private formBuilder: FormBuilder,
    private router: Router
  ) { }

  ngOnInit() {
    this.router.onSameUrlNavigation = "reload"
    this.PresencaForm = this.formBuilder.group({
      id : this.formBuilder.control('',[Validators.required]),
      dia : this.formBuilder.control('',[Validators.required]),
      situacao : this.formBuilder.control('',[Validators.required]),

      aluno : this.formBuilder.control(
        AlunoService.getCurrAluno(),
        [Validators.required]
      ),
      aula : this.formBuilder.control(
        AulaService.getCurrAula(),
        [Validators.required]
      ),

    })

  }
}

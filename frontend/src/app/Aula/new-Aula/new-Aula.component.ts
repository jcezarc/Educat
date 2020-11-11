import { Component, OnInit } from '@angular/core';
import { AulaModel } from '../Aula-model';
import { AulaService } from '../Aula-service';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import {ProfessorService} from '../../Professor/Professor-service'


@Component({
  selector: 'app-new-Aula',
  templateUrl: './new-Aula.component.html'
})
export class NewAulaComponent implements OnInit {

  AulaForm: FormGroup

  constructor(
    private AulaSvc: AulaService,
    private formBuilder: FormBuilder,
    private router: Router
  ) { }

  ngOnInit() {
    this.router.onSameUrlNavigation = "reload"
    this.AulaForm = this.formBuilder.group({
      id : this.formBuilder.control('',[Validators.required]),
      descricao : this.formBuilder.control('',[Validators.required]),
      sala : this.formBuilder.control('',[Validators.required]),
      horario : this.formBuilder.control('',[Validators.required]),
      logotipo : this.formBuilder.control('',[Validators.required]),

      professor : this.formBuilder.control(
        ProfessorService.getCurrProfessor(),
        [Validators.required]
      ),

    })

        this.AulaForm.get('id').valueChanges.subscribe(
        newValue => {
            this.AulaForm.get('logotipo').setValue(
            `assets/img/Aula/${newValue}.jpg`
            )
        }
        )
                
  }
}

import { Component, OnInit } from '@angular/core';
import { AlunoModel } from '../Aluno-model';
import { AlunoService } from '../Aluno-service';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { Router } from '@angular/router';


@Component({
  selector: 'app-new-Aluno',
  templateUrl: './new-Aluno.component.html'
})
export class NewAlunoComponent implements OnInit {

  AlunoForm: FormGroup

  constructor(
    private AlunoSvc: AlunoService,
    private formBuilder: FormBuilder,
    private router: Router
  ) { }

  ngOnInit() {
    this.router.onSameUrlNavigation = "reload"
    this.AlunoForm = this.formBuilder.group({
      RA : this.formBuilder.control('',[Validators.required]),
      nome : this.formBuilder.control('',[Validators.required]),
      obs : this.formBuilder.control('',[Validators.required]),
      foto : this.formBuilder.control('',[Validators.required]),


    })

        this.AlunoForm.get('RA').valueChanges.subscribe(
        newValue => {
            this.AlunoForm.get('foto').setValue(
            `assets/img/Aluno/${newValue}.jpg`
            )
        }
        )
                
  }
}

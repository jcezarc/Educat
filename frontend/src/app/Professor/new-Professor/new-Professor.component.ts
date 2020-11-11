import { Component, OnInit } from '@angular/core';
import { ProfessorModel } from '../Professor-model';
import { ProfessorService } from '../Professor-service';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { Router } from '@angular/router';


@Component({
  selector: 'app-new-Professor',
  templateUrl: './new-Professor.component.html'
})
export class NewProfessorComponent implements OnInit {

  ProfessorForm: FormGroup

  constructor(
    private ProfessorSvc: ProfessorService,
    private formBuilder: FormBuilder,
    private router: Router
  ) { }

  ngOnInit() {
    this.router.onSameUrlNavigation = "reload"
    this.ProfessorForm = this.formBuilder.group({
      RF : this.formBuilder.control('',[Validators.required]),
      nome : this.formBuilder.control('',[Validators.required]),
      especialidade : this.formBuilder.control('',[Validators.required]),
      foto : this.formBuilder.control('',[Validators.required]),


    })

        this.ProfessorForm.get('RF').valueChanges.subscribe(
        newValue => {
            this.ProfessorForm.get('foto').setValue(
            `assets/img/Professor/${newValue}.jpg`
            )
        }
        )
                
  }
}

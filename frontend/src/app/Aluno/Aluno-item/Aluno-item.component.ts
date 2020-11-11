import { Component, OnInit, Input } from '@angular/core';
import { AlunoModel } from '../Aluno-model';

@Component({
  selector: 'app-Aluno-item',
  templateUrl: './Aluno-item.component.html',
  styleUrls: ['./Aluno-item.component.css']
})
export class AlunoItemComponent implements OnInit {

  @Input() Aluno: AlunoModel

  constructor() { }

  ngOnInit() {
  }

}

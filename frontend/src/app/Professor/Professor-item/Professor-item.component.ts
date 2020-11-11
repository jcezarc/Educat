import { Component, OnInit, Input } from '@angular/core';
import { ProfessorModel } from '../Professor-model';

@Component({
  selector: 'app-Professor-item',
  templateUrl: './Professor-item.component.html',
  styleUrls: ['./Professor-item.component.css']
})
export class ProfessorItemComponent implements OnInit {

  @Input() Professor: ProfessorModel

  constructor() { }

  ngOnInit() {
  }

}

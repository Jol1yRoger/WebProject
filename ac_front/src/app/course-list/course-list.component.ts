import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { CoursesService } from '../courses.service';

@Component({
  selector: 'app-course-list',
  templateUrl: './course-list.component.html',
  styleUrl: './course-list.component.css'
})
export class CourseListComponent implements OnInit {

    courses$!: Observable<any[]>;
    constructor(private coursesService: CoursesService) {}

    ngOnInit(): void {
      this.courses$ = this.coursesService.getCourses();
    }

}

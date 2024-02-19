import { Component, OnInit } from '@angular/core';
import { IcourseInterface } from '../icourse.interface';
import { CourseService } from '../course.service';

@Component({
  selector: 'app-raptor-course-list',
  templateUrl: './raptor-course-list.component.html',
  styleUrls: ['./raptor-course-list.component.css'],
})
export class RaptorCourseListComponent implements OnInit {
  allCourses: IcourseInterface[] = [];
  constructor(private courseService: CourseService) {}
  ngOnInit(): void {
    this.getCourses();
  }

  getCourses(): void {
    this.courseService.getAllCourses().subscribe((courses) => {
      this.allCourses = courses;
    });
  }
}

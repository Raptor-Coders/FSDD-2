import { Component, OnInit } from '@angular/core';
import { COURSES } from '../courses-data';
import { ActivatedRoute, ActivatedRouteSnapshot } from '@angular/router';
import { CourseService } from '../course.service';

@Component({
  selector: 'app-course-details',
  templateUrl: './course-details.component.html',
  styleUrls: ['./course-details.component.css'],
})
export class CourseDetailsComponent implements OnInit {
  // course: any = {};
  coursesByID: any = [];
  // id: any;

  constructor(
    private courseService: CourseService,
    private route: ActivatedRoute
  ) {

   
    // const id: number = +route.snapshot.params['id'];
    // console.log(id)
    // for (let course of COURSES) {
    //   if (course.id === id) {
    //     this.course = course;
    //   }
    // }
    // this.coursesByID = courseService.getCourseById(id);
    // console.log(this.coursesByID)
  }
  ngOnInit(): void {
    const id: number = +this.route.snapshot.params['id'];
    this.getCourseById(id);
     console.log(id);
    
  }
  getCourseById(id:number) {
    // this.id = this.route.snapshot.params['id'];
    console.log(id);
    this.courseService.getCourseById(id).subscribe((courses) => {
      this.coursesByID = courses;
    });
  }
}

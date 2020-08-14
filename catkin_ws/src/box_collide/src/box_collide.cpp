#include <moveit/move_group_interface/move_group.h>
#include <moveit/planning_scene_interface/planning_scene_interface.h>
#include <geometric_shapes/shape_operations.h>

using namespace Eigen; 

int main(int argc, char **argv)
{
    ros::init(argc, argv, "add_wall");
    ros::NodeHandle nh;
    ros::AsyncSpinner spin(1);
    spin.start();

    moveit::planning_interface::PlanningSceneInterface current_scene;
    sleep(2.0);

    Vector3d b(0.001, 0.001, 0.001);
    moveit_msgs::CollisionObject co;
    co.id = "wall";
    shapes::Mesh* m = shapes::createMeshFromResource("package://mitsubishi_rv6sd_support/meshes/wall.stl",b); 
    ROS_INFO("Wall mesh loaded");

    shape_msgs::Mesh mesh;
    shapes::ShapeMsg mesh_msg;  
    shapes::constructMsgFromShape(m, mesh_msg);
    mesh = boost::get<shape_msgs::Mesh>(mesh_msg);

    co.meshes.resize(1);
    co.mesh_poses.resize(1);
    co.meshes[0] = mesh;
    co.header.frame_id = "wall";   
    co.mesh_poses[0].position.x = 0.560651;
    co.mesh_poses[0].position.y = 0.579113;
    co.mesh_poses[0].position.z = 0.0;
    co.mesh_poses[0].orientation.w= 0.0; 
    co.mesh_poses[0].orientation.x= 0.0; 
    co.mesh_poses[0].orientation.y= 0.0;
    co.mesh_poses[0].orientation.z= 0.0;   

    co.meshes.push_back(mesh);
    co.mesh_poses.push_back(co.mesh_poses[0]);
    co.operation = co.ADD;
    std::vector<moveit_msgs::CollisionObject> vec;
    vec.push_back(co);
    ROS_INFO("Wall added into the world");
    current_scene.addCollisionObjects(vec);
    sleep(5.0);
    ros::shutdown();
    return 0;
}
